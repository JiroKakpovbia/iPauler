from textgenrnn import textgenrnn
import tempfile

def get_tweet(prefix="Paulers"):
    textgen = textgenrnn(weights_path='colaboratory_weights.hdf5',
                           vocab_path='colaboratory_vocab.json',
                           config_path='colaboratory_config.json')
    with tempfile.NamedTemporaryFile() as tmp:
        textgen.generate_to_file(tmp.name, n=1, temperature=[0.7], max_gen_length=150, prefix=prefix)
        tweet = open(tmp.name).read()
    return tweet
