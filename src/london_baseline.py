# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils 
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

correct = 0
total = 0
#with open(args.outputs_path, 'w') as fout:
predictions = []
for line in open(args.eval_corpus_path):
    pred = "London"
    # completion = ''.join([pretrain_dataset.itos[int(i)] for i in pred])
    # pred = completion.split('⁇')[1]
    predictions.append(pred)
    # fout.write(pred + '\n')
total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))

