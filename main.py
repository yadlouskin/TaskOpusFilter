from datafiles import FilesWrapper

from opusfilter import word_alignment
from opusfilter.embeddings import *




def main():
    sent_emb_filter = SentenceEmbeddingFilter(languages=['en', 'ru'], threshold=0.9)
    align_filter = word_alignment.WordAlignFilter(src_threshold=10, tgt_threshold=10,
                                                  src_tokenizer=['moses', 'en'], tgt_tokenizer=['moses', 'ru'])

    with FilesWrapper(lines_limit=10) as data:
        for en, ru in data:
            print('\nen: ', en, '\nru: ', ru)
            row = [(en, ru)]
            total = True

            score = next(sent_emb_filter.score(row))
            accepted = sent_emb_filter.accept(score)
            total &= accepted
            print('SentenceEmbeddingFilter')
            print('score:  ', score)
            print('accepted: ', accepted)


            score = next(align_filter.score(row))
            accepted = align_filter.accept(score)
            total &= accepted
            print('WordAlignFilter')
            print('scores: ', score)
            print('accepted: ', accepted)

            print('Total: ', total)
            if total:
                data.write_line()


if __name__ == "__main__":
    main()

