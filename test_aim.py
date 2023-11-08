from aim import Run


run = Run()
hparams_dict = {
    'learning_rate': 0.001,
    'batch_size': 32,
}
run['hparams'] = hparams_dict

# log metric
for i in range(10):
    run.track(i, name='numbers')