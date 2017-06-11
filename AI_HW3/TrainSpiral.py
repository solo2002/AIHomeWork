# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Trains a network using preloaded data in a constant."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import time

import Q14GenerateDataGraph
import tensorflow as tf

import network

# Put your data and labels here
training_data = []
training_labels = []
#Q14TensorFlow.gauss_data(100, training_data, training_labels)
#Q14TensorFlow.circle_data(100, training_data, training_labels)
#Q14TensorFlow.xor_data(100, training_data, training_labels)
Q14GenerateDataGraph.spiral_data(100, training_data, training_labels)

# Basic model parameters as external flags.
FLAGS = None

def run_training():
  """Train network for a number of epochs."""
  # Tell TensorFlow that the model will be built into the default Graph.
  with tf.Graph().as_default():
    with tf.name_scope('input'):
      # Input data, pin to CPU because rest of pipeline is CPU-only
      with tf.device('/cpu:0'):
        input_data = tf.constant(training_data)
        input_labels = tf.constant(training_labels)

      input, label = tf.train.slice_input_producer(
        [input_data, input_labels], num_epochs=FLAGS.num_epochs)
      label = tf.cast(label, tf.int32)
      input, labels = tf.train.batch([input, label], batch_size=FLAGS.batch_size)

      # Build a Graph that computes predictions from the inference model.
      logits = network.inference(input, FLAGS.hidden1, FLAGS.hidden2)

      # Add to the Graph the Ops for loss calculation.
      loss = network.loss(logits, labels)

      # Add to the Graph the Ops that calculate and apply gradients.
      train_op = network.training(loss, FLAGS.learning_rate)

      # Add the Op to compare the logits to the labels during evaluation.
      eval_correct = network.evaluation(logits, labels)

      # Build the summary operation based on the TF collection of Summaries.
      summary_op = tf.summary.merge_all()

      # Create a saver for writing training checkpoints.
      saver = tf.train.Saver()

      # Create the op for initializing variables.
      init_op = tf.group(tf.global_variables_initializer(),
                         tf.local_variables_initializer())
      # Create a session for running Ops on the Graph.
      sess = tf.Session()

      # Run the Op to initialize the variables.
      sess.run(init_op)

      # Instantiate a SummaryWriter to output summaries and the Graph.
      summary_writer = tf.train.SummaryWriter(FLAGS.train_dir, sess.graph)

      # Start input enqueue threads.
      coord = tf.train.Coordinator()
      threads = tf.train.start_queue_runners(sess=sess, coord=coord)

      # And then after everything is built, start the training loop.
  for ep in xrange(FLAGS.num_epochs):
    for step in xrange(FLAGS.max_steps):
      start_time = time.time()
      _, loss_value = sess.run([train_op, loss])
      duration = time.time() - start_time
      # Write the summaries and print an overview fairly often.
      if loss_value - 0.0 <= 0.00001:
        print('Loss value: %.4f, done training for %d epochs, %d steps.' % (loss_value, ep, ep * FLAGS.max_steps + step))
        return
      if step % 100 == 0:
        # Print status to stdout.
        print('Epochs %d: loss = %.4f (%.3f sec)' % (ep, loss_value,
                                                   duration))
        # Update the events file.
        summary_str = sess.run(summary_op)
        summary_writer.add_summary(summary_str, step)

        # Save a checkpoint periodically.
        if (step + 1) % 1000 == 0 or (step + 1) == FLAGS.max_steps:
          print('Saving')
          saver.save(sess, FLAGS.train_dir, global_step=step)

# the following code stops after 2 steps
  # try:
  #   step = 0
  #   while not coord.should_stop():
  #     start_time = time.time()
  #
  #     # Run one step of the model.
  #     _, loss_value = sess.run([train_op, loss])
  #
  #     duration = time.time() - start_time
  #
  #     # Write the summaries and print an overview fairly often.
  #     if step % 100 == 0:
  #       # Print status to stdout.
  #       print('Step %d: loss = %.2f (%.3f sec)' % (step, loss_value,
  #                                                  duration))
  #       # Update the events file.
  #       summary_str = sess.run(summary_op)
  #       summary_writer.add_summary(summary_str, step)
  #       step += 1
  #
  #       # Save a checkpoint periodically.
  #       if (step + 1) % 1000 == 0 or (step + 1) == FLAGS.max_steps:
  #         print('Saving')
  #         saver.save(sess, FLAGS.train_dir, global_step=step)
  #       step += 1
  #
  # except tf.errors.OutOfRangeError:
  #   print('Saving')
  #   saver.save(sess, FLAGS.train_dir, global_step=step)
  #   print('Done training for %d epochs, %d steps.' % (FLAGS.num_epochs, step))
  # finally:
  #   # When done, ask the threads to stop.
  #   coord.request_stop()
  #
  #   # Wait for threads to finish.
  #   coord.join(threads)
  #   sess.close()


def main(_):
  run_training()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--learning_rate',
    type=float,
    default=0.02,
    help='Initial learning rate.'
  )
  parser.add_argument(
    '--max_steps',
    type=int,
    default=100,
    help='Number of steps to run trainer.'
  )

  parser.add_argument(
    '--num_epochs',
    type=int,
    default=200,
    help='Number of epochs.'
  )
  parser.add_argument(
    '--hidden1',
    type=int,
    default=5,
    help='Number of units in hidden layer 1.'
  )
  parser.add_argument(
    '--hidden2',
    type=int,
    default=5,
    help='Number of units in hidden layer 2.'
  )
  parser.add_argument(
    '--batch_size',
    type=int,
    default=1,
    help='Batch size.  Must divide evenly into the dataset sizes.'
  )
  # parser.add_argument(
  #   '--input_data_dir',
  #   type=str,
  #   default='/tmp/tensorflow/mnist/input_data',
  #   help='Directory to put the input data.'
  # )
  parser.add_argument(
    '--train_dir',
    type=str,
    default='train_summary',
    help='Directory to put the log data.'
  )
  # parser.add_argument(
  #   '--fake_data',
  #   default=False,
  #   help='If true, uses fake data for unit testing.',
  #   action='store_true'
  # )

  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)