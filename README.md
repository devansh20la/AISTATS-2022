# Low-Pass Filtering SGD for Recovering Flat Optima in the Deep Learning Optimization Landscape

This repository is the official implementation of Low-Pass Filtering SGD for Recovering Flat Optima in the Deep Learning Optimization Landscape. 


## Requirements

To install requirements:

```setup
create --name <env> --file requirement.txt
```


## Sharpness vs generalization:

All the training codes and computing sharpness measures lie in the folder sharpness_v_generalization:

```train
./run.sh
```

This shell script will perform the following operations:
1. Download all relevant datasets.
2. Train 2916 resnet18 models on cifar10 dataset with varying hyper-parameters and 3 random seeds.
3. Train 50 different models with 10 different level of label noise and 5 random seeds.
4. Train 100 different models with 20 different level of data noise and 5 random seeds.
5. Train 64 different models with 64 different width levels and 5 random seeds.
6. Compute sharpness measures for all the models and store it as a numpy array in .pkl file 


## Experiments 1

### Training
We can train sgd, sam and lpfsgd models on cifar10 data with resnet18 model as follow:

```
	python sgd_train.py \
		--ep=200 \
		--bs=128 \
		--dtype='cifar10' \
		--mtype='resnet18' \
		--print_freq=100 \
		--mo=0.9 \
		--lr=0.1 \
		--ms=0 \
		--wd=5e-4
```

We can train sam models as:

```
	python sam_train.py \
		--ep=200 \
		--bs=128 \
		--dtype='cifar10' \
		--mtype='resnet18' \
		--print_freq=100 \
		--mo=0.9 \
		--lr=0.1 \
		--ms=0 \
		--wd=5e-4
```

We can train lpfsgd models as:

```
	python lpf_train.py \
		--ep=200 \
		--bs=128 \
		--dtype='cifar10' \
		--mtype='resnet18' \
		--print_freq=100 \
		--mo=0.9 \
		--lr=0.1 \
		--ms=0 \
		--wd=5e-4
```

### Hyper-parameters
\begin{table}[H]
    \setlength\tabcolsep{2.2pt}
    \renewcommand{\arraystretch}{1.3}
    \centering
    \begin{tabular}{|c|c|c|c|c|c|c|}
        \hline
        Dataset & Model & BS & WD & MO & Epochs  & LR (Policy)\\ \hline
        MNIST & LeNet & 128 & $5e^{-4}$ & 0.9 & 150 & 0.01 (x 0.1 at ep=[50,100])  \\ 
        CIFAR10, 100 & ResNet-18, 50, 101 & 128 & $5e^{-4}$ & 0.9 & 200 & 0.1 (x 0.1 at ep=[100,120])  \\ 
        TinyImageNet & ResNet-18 & 128 & $1e^{-4}$ & 0.9 & 100 & 0.1 (x 0.1 at ep=[30, 60, 90]) \\ 
        ImageNet & ResNet-18 & 256 & $1e^{-4}$ & 0.9 & 100 & 0.1 (x 0.1 at ep=[30, 60, 90]) \\ \hline
    \end{tabular}
    \caption{Training hyper-parameters common to all optimizers utilized for Table~\ref{tab:exp1}.Here BS: batch size, WD: weight decay, MO: SGD momentum.}
    \label{tab:exp1_1}
\end{table}

\begin{table}[H]
    \setlength\tabcolsep{2.2pt}
    \renewcommand{\arraystretch}{1.3}
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        Dataset & Model & $\rho$ (policy) \\ \hline
        MNIST & LeNet & 0.05 (fixed) \\
        CIFAR & ResNet18,50,101 & 0.05 (fixed) \\ 
        TinyImageNet & ResNet18 & 0.05 (fixed) \\ 
        ImageNet & ResNet18 & 0.05 (fixed) \\ \hline
    \end{tabular}
    \caption{Summary of SAM hyper-parameters utilized for table~\ref{tab:exp1}.}
    \label{tab:exp1_3}
\end{table}

## Experiments 2


