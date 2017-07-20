import pymongo
import tensorflow as tf
import numpy as np
import os
import time
import datetime
import PROJ_COD.Machine.lee.data_helpers as data_helpers
from PROJ_COD.Machine.lee.text_cnn import TextCNN
from tensorflow.contrib import learn

connection = pymongo.MongoClient("mongodb://203.234.103.169")
db = connection.maldb   #db 이름 악성코드모아놓은곳
learning_data = db.learning_data #이것도 db 인데 학습시킬애들인가

# Parameters
# ==================================================

# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding (default: 128)")
tf.flags.DEFINE_string("filter_sizes", "2,3,4", "Comma-separated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "L2 regularizaion lambda (default: 0.0)")

# Training parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_integer("num_epochs", 200, "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 20, "Evaluate model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", 200, "Save model after this many steps (default: 100)")
# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")
# flags 얘네들은 뭐 그냥 define 이라고 생각하면 됨

# Data Preparatopn
# ==================================================
# Load data


def get_sample_data():
    text = []
    label = []
    r_label = []
    detect_and_num = {}
    learn_data = learning_data.find()   #이거도 이름바꾸
    for line in learn_data:
        text_val = line["opcode"].keys() + line["ie_api"] + line["section_info"].keys() #opcode, api, section_info 저장
        detect_val = line['detect'].split(".")[0]
        # detect_val = line['detect']
        text.append(" ".join(str(e) for e in text_val)) #text에 아까 불러왔던애들 저장

        if len(detect_and_num) == 0:
            detect_and_num[detect_val] = 1 # detect_and_num[바이러스이름 = 1  을 뜻하는듯

        if detect_val not in detect_and_num.keys(): # 바이러스이름이 keys 에 없으면
            current_max = detect_and_num[max(detect_and_num, key=detect_and_num.get)] # 만들고 추가하고
            detect_and_num[detect_val] = current_max + 1    # 값 하나 올리고

        label.append(detect_and_num[detect_val])  #label에 저장하네 위에서 구한결과

    max_num = max(label)  #그 후 max값 변경.
    for l_num in label:
        lst = [0 for _ in range(max_num)]
        lst[-l_num] = 1
        r_label.append(lst)  #lst 범위 max_num까지 다 1로 바꾸고 r_label에 저장

    r_label = np.array(r_label)
    return text, r_label, detect_and_num # text=opcode,api,section_info , r_label= 악성코드종류갯수? detect_and_num = 탐지갯수 같은데


print("Loading data...")
x_text, y, dict_z = get_sample_data() # x_text = text , y = r_label , dict_z = detect_and_num

# Build vocabulary
max_document_length = max([len(x.split(" ")) for x in x_text]) # 길이를 왜 구하지
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length) # 길이가 다른 문서를 max_document_length로 맞춰주는 역할
x = np.array(list(vocab_processor.fit_transform(x_text))) # x = x_text 마다 단어를 숫자순서로 바꿔서 숫자로 순서 나열해놓은거

# Randomly shuffle data
np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(y)))
x_shuffled = x[shuffle_indices]
y_shuffled = y[shuffle_indices] # 0부터 y 길이까지 데이터를 섞는다.

# Split train/test set
# TODO: This is very crude, should use cross-validation
cut = int(len(x_shuffled) * 0.90) # x_shuffled 길이 * 0.9 = cut

x_train, x_dev = x_shuffled[:cut], x_shuffled[cut:] # 왜 한놈을 앞뒤로잘라넣는진 모르겠지만 어쩃든
y_train, y_dev = y_shuffled[:cut], y_shuffled[cut:] # 뒤잘라넣고 앞잘라넣고
print("Data Size: {:d}".format(len(x_shuffled))) # x == opcode
print("Label Size: {:d}".format(len(dict_z))) # dict_z == detect_and_num   파일갯수일듯?
print("Vocabulary Size: {:d}".format(len(vocab_processor.vocabulary_))) # 단어사전의 길이인듯
print("Train/Dev split: {:d}/{:d}".format(len(y_train), len(y_dev))) #
# data set make end




# Training
# ==================================================

with tf.Graph().as_default():
    session_conf = tf.ConfigProto(  #  https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/core/protobuf/config.proto
        allow_soft_placement=FLAGS.allow_soft_placement,
        log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        cnn = TextCNN(
            sequence_length=x_train.shape[1],
            num_classes=y_train.shape[1],
            vocab_size=len(vocab_processor.vocabulary_),
            embedding_size=FLAGS.embedding_dim,
            filter_sizes=list(map(int, FLAGS.filter_sizes.split(","))),
            num_filters=FLAGS.num_filters,
            l2_reg_lambda=FLAGS.l2_reg_lambda)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss) # gradient 계산값 구하여 수동 적용  , gradient == 기울기
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step) # grads_and_vars 수정

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            if g is not None: #  그래프 정의시 필요한 scalar 값마다 summary
                grad_hist_summary = tf.histogram_summary("{}/grad/hist".format(v.name), g) # histogram == 학습과정 시각화때 사용할 데이터 직렬화하기위한 메소드
                sparsity_summary = tf.scalar_summary("{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g)) # scalar == 학습과정을 시각화할 때 사용할 데이터를 직렬화 하기위한 메소드
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
        grad_summaries_merged = tf.merge_summary(grad_summaries) # histogram, scalar 통합.

        # Output directory for models and summaries
        timestamp = str(int(time.time())) # 시간을 초 단위로 부동소수점 숫자로 변환
        out_dir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp)) # runs디렉토리 경로 == out_dir
        print("Writing to {}\n".format(out_dir)) # runs디렉토리 경로 print

        # Summaries for loss and accuracy
        loss_summary = tf.scalar_summary("loss", cnn.loss) # scalar 로 변수를 요약 "loss" "accuracy" 이런건 태그라고 함
        acc_summary = tf.scalar_summary("accuracy", cnn.accuracy)

        # Train Summaries
        train_summary_op = tf.merge_summary([loss_summary, acc_summary, grad_summaries_merged]) # summary 통합
        train_summary_dir = os.path.join(out_dir, "summaries", "train") # session 생성
        train_summary_writer = tf.train.SummaryWriter(train_summary_dir, sess.graph) # summarywriter 정의

        # Dev summaries
        dev_summary_op = tf.merge_summary([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
        dev_summary_writer = tf.train.SummaryWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints")) #
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir) # 디렉터리 생성
        saver = tf.train.Saver(tf.all_variables()) # 오퍼레이션을 실행하는 메서드와 읽고 쓰는 체크포인트 파일의 지정된 경로를 제공

        # Write vocabulary
        vocab_processor.save(os.path.join(out_dir, "vocab")) #

        # Initialize all variables
        sess.run(tf.initialize_all_variables()) # 모든 변수를 병렬로 초기화


        def train_step(x_batch, y_batch):
            """
            A single training step
            """
            feed_dict = {
                cnn.input_x: x_batch,
                cnn.input_y: y_batch,
                cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
            }
            _, step, summaries, loss, accuracy = sess.run(
                [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            train_summary_writer.add_summary(summaries, step)


        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            feed_dict = {
                cnn.input_x: x_batch,
                cnn.input_y: y_batch,
                cnn.dropout_keep_prob: 1.0
            }
            step, summaries, loss, accuracy, predictions = sess.run(
                [global_step, dev_summary_op, cnn.loss, cnn.accuracy, cnn.predictions],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))

            # compare data
            max_dict_z = dict_z[max(dict_z, key=lambda i: dict_z[i])]
            predict_list = []
            true_list = []
            o_x_list = []
            for one_predict in predictions:
                predict_list.append(dict_z.keys()[dict_z.values().index(max_dict_z - one_predict)])

            for one_batch in y_batch:
                true_list.append(dict_z.keys()[dict_z.values().index(max_dict_z - one_batch.tolist().index(1))])

            for num in range(len(predict_list)):
                if predict_list[num] == true_list[num]:
                    o_x_list.append("O")
                else:
                    o_x_list.append("X")

            print("[+] Ahnlab-V3 Detection [+]")
            print(true_list)
            print("")
            print("[+] Machine Detection [+]")
            print(predict_list)
            print("")
            print(o_x_list)

            if writer:
                writer.add_summary(summaries, step)


        # Generate batches
        batches = data_helpers.batch_iter(
            list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)
            train_step(x_batch, y_batch)
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                print("\nEvaluation:")
                dev_step(x_dev, y_dev, writer=dev_summary_writer)
                print("")
            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))