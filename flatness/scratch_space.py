# import glob

# for fol in glob.glob("*sgd_*"):
#     for file in glob.glob(fol + "/run_ms_0/*.log"):
#         f = open(file, 'r')
#         cont = f.read()
#         if 'nan' in cont:
#             print(file)

# from sklearn.model_selection import ParameterGrid

# param_grid = {'ms': [0],  # seed
#               'mo': [0.0, 0.5, 0.9],  # momentum
#               'width': [4, 6, 8],  # network width
#               'wd': [0.0, 1e-4, 1e-2],  # weight decay
#               'lr': [5e-3, 1e-2, 5e-2],  # learning rate
#               'bs': [16, 32, 64],  # batch size
#               'lr_decay': [True, False],  # learning rate decay
#               'skip': [True, False],  # skip connection
#               'batchnorm': [True, False]  # batchnorm
#               }

# grid = list(ParameterGrid(param_grid))
# fols = glob.glob1("."/ "*sgd_*")

# for i,param in enumerate(grid,0):
#   n = f"{i}_{param['width']}_{param['batchnorm']}_{param['skip']}_" \
#       f"{param['optim']}_{param['ep']}_{param[lr}_{param['wd']}_" \
#       f"{param['bs']}_{param['mo']}_{param['lr_decay']}"

#   with open(n + '')
#   print()


import glob

with open("results/resnet_cifar10.csv", 'w') as f:
    f.write("exp_num, width,batchnorm,skip,opt, epoch, lr,wd,bs,mo,lr-decay,train_loss, train_err, val_loss,val_err, flatness, div\n")

for fol in glob.glob("checkpoints/all_new_cifar10/*sgd_*"):
    with open(fol + "/run_ms_0/dist_bw_params.txt", 'r') as f:
        h = next(f)
        cont = next(f)
    with open("results/resnet_cifar10.csv", 'a') as f:
        f.write(f"{','.join(fol.split('/')[-1].split('_'))}, {cont}")
