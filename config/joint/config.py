import os

class Config:
    def get_labels_length(self, file_path):
        """
        Returns the number of labels in a file.

        Args:
            file_path (str): The path to the file containing the labels.

        Returns:
            int: The number of labels in the file.
        """
        with open(file_path) as f:
            return len(tuple(line.strip() for line in f.readlines()))

    #### PATH ####
    ROOT_DIR            = os.path.dirname(os.path.abspath("__file__"))
    DATA_DIR            = ROOT_DIR + "/data/youdao/"
    train_data_path     = DATA_DIR + "train_am/datalist.jsonl"
    valid_data_path     = DATA_DIR + "valid_am/datalist.jsonl"
    output_directory    = ROOT_DIR + "/outputs"
    speaker2id_path     = DATA_DIR + "text/speaker2"
    emotion2id_path     = DATA_DIR + "text/emotion"
    pitch2id_path       = DATA_DIR + "text/pitch"
    energy2id_path      = DATA_DIR + "text/energy"
    speed2id_path       = DATA_DIR + "text/speed"
    bert_path           = 'WangZeJun/simbert-base-chinese'
    token_list_path     = DATA_DIR + "text/tokenlist"
    style_encoder_ckpt  = ROOT_DIR + "/outputs/style_encoder/ckpt/checkpoint_163431"
    tmp_dir             = ROOT_DIR + "/tmp"
    model_config_path   = ROOT_DIR + "/config/joint/config.yaml"

    #### Model ####
    bert_hidden_size = 768
    style_dim = 128
    downsample_ratio    = 1     # Whole Model

    #### Text ####
    n_symbols           = get_labels_length(token_list_path)
    sep                 = " "

    #### Speaker ####
    speaker_n_labels = get_labels_length(speaker2id_path)

    #### Emotion ####
    emotion_n_labels = get_labels_length(emotion2id_path)

    #### Speed ####
    speed_n_labels = get_labels_length(speed2id_path)

    #### Pitch ####
    pitch_n_labels = get_labels_length(pitch2id_path)

    #### Energy ####
    energy_n_labels = get_labels_length(energy2id_path)

    #### Train ####
    # epochs              = 10
    lr                  = 1e-3
    lr_warmup_steps     = 4000
    kl_warmup_steps     = 60_000
    grad_clip_thresh    = 1.0
    batch_size          = 16
    train_steps         = 10_000_000
    opt_level           = "O1"
    seed                = 1234
    iters_per_validation= 1000
    iters_per_checkpoint= 10000


    #### Audio ####
    sampling_rate       = 16_000
    max_db              = 1
    min_db              = 0
    trim                = True

    #### Stft ####
    filter_length       = 1024
    hop_length          = 256
    win_length          = 1024
    window              = "hann"

    #### Mel ####
    n_mel_channels      = 80
    mel_fmin            = 0
    mel_fmax            = 8000

    #### Pitch ####
    pitch_min           = 80
    pitch_max           = 400
    pitch_stats         = [225.089, 53.78]

    #### Energy ####
    energy_stats        = [30.610, 21.78]


    #### Infernce ####
    gta                 = False