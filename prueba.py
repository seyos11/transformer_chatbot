import random
import torch
from torch.utils.data import Dataset
from model.text import BPEVocab
from model.dataset import FacebookDataset

with open('convai2_fix_723/train_self_revised_no_cands.txt', 'r', encoding='utf-8') as file:
            data = []
            for line in file.readlines():
                line = line.strip()

                if len(line) == 0:
                    continue

                space_idx = line.find(' ')
                if space_idx == -1:
                    dialog_idx = int(line)
                else:
                    dialog_idx = int(line[:space_idx])

                if int(dialog_idx) == 1:
                    data.append({'persona_info': [], 'dialog': []})

                dialog_line = line[space_idx + 1:].split('\t')
                dialog_line = [l.strip() for l in dialog_line]

                if dialog_line[0].startswith('your persona:'):
                    persona_info = dialog_line[0].replace('your persona: ', '')
                    data[-1]['persona_info'].append(persona_info)

                elif len(dialog_line) > 1:
                    data[-1]['dialog'].append(dialog_line[0])
                    data[-1]['dialog'].append(dialog_line[1])
def make_dataset(data, vocab, max_lengths):
        dataset = []
        for chat in data:
            persona_info = [vocab.string2ids(s) for s in chat['persona_info']]
            dialog = [vocab.string2ids(s) for s in chat['dialog']]

            if len(dialog) % 2 == 1:
                dialog = dialog[:-1]
           
            dataset.append((persona_info, dialog))

        return dataset

vocab = BPEVocab.from_files('./parameters/bpe.vocab', './parameters/bpe.vocab')
data_updated =make_dataset(data, vocab, 511)