import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import accuracy_score

data = pd.read_csv('avocado_data.csv')

features = data.drop(['Date', 'type', 'region', 'AveragePrice'], axis=1)
labels = data['type']

data = data.dropna()

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)
y_tensor = torch.tensor(y_encoded, dtype=torch.long)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

class AvocadoClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AvocadoClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

input_size = X_tensor.shape[1]
hidden_size = 64
output_size = len(label_encoder.classes_)
epochs = 10
lr = 0.00001
log_interval = 10

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AvocadoClassifier(input_size, hidden_size, output_size).to(device)
optimizer = optim.SGD(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss()

def train(model, device, train_loader, optimizer, criterion, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

for epoch in range(1, epochs + 1):
    train(model, device, train_loader, optimizer, criterion, epoch)

model.eval()
with torch.no_grad():
    y_pred = torch.argmax(model(X_test.to(device)), dim=1).cpu().numpy()

accuracy = accuracy_score(y_test.numpy(), y_pred)
print(f'Accuracy: {accuracy}')
