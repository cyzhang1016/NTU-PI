import os
import torch
import numpy as np
from torch import nn
from torch.utils.data import DataLoader,Dataset

dtype = np.float32

class myDataset(Dataset):
    def __init__(self,X,y):
        super().__init__()
        self.X = X
        self.y = y
           
    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return len(self.X) 
        
 
class MLP(nn.Module):
    '''
        Multilayer Perceptron.
    '''
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(3, 4),
            nn.ReLU(),
            nn.Linear(4, 4),
            nn.ReLU(),
            nn.Linear(4, 1)
        )


    def forward(self, x):
        '''Forward pass'''
        return torch.squeeze(self.layers(x))
  
def read(path):
    X = np.loadtxt(path,dtype=dtype,skiprows=1)
    return torch.tensor(X)


def train(mlp):
    trainX = read("train_data.txt")
    trainY = read("train_truth.txt")
    dataset = myDataset(trainX,trainY)
    trainloader = torch.utils.data.DataLoader(dataset, batch_size=10, shuffle=True, num_workers=1)
    
    # Define the loss function and optimizer
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(mlp.parameters(), lr=1e-4)
    
    # Run the training loop
    for epoch in range(0, 5): # 5 epochs at maximum
        
        # Print epoch
        print(f'Starting epoch {epoch+1}')
        
        # Set current loss value
        current_loss = 0.0
        
        # Iterate over the DataLoader for training data
        for i, data in enumerate(trainloader, 0):
        
            # Get inputs
            inputs, targets = data
            
            # Zero the gradients
            optimizer.zero_grad()
            
            # Perform forward pass
            outputs = mlp(inputs)
            
            # Compute loss
            loss = loss_function(outputs, targets)
            
            # Perform backward pass
            loss.backward()
            
            # Perform optimization
            optimizer.step()
        
            # Print statistics
            current_loss += loss.item()
            if i % 500 == 499:
                print('Loss after mini-batch %5d: %.3f' %
                        (i + 1, current_loss / 500))
                current_loss = 0.0

    # Process is complete.
    print('Training process has finished.')

def test(mlp):
    testX = read("test_data.txt")
    outputs = mlp(testX).detach().numpy()
    np.savetxt("test_predicted.txt",outputs,header="y",comments="")
  
if __name__ == '__main__':
  
    # Set fixed random number seed
    torch.manual_seed(42)

    # Initialize the MLP
    mlp = MLP()
    train(mlp)
    test(mlp)

#Online materials:https://www.machinecurve.com/index.php/2021/01/26/creating-a-multilayer-perceptron-with-pytorch-and-lightning/