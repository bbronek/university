from data import load_data
from sklearn.metrics import accuracy_score
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


class AvocadoClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, values):
        return self.layers(values)


def main():
    torch.manual_seed(42)
    train, test, train_labels, test_labels, classes = load_data()
    dataset = TensorDataset(
        torch.tensor(train, dtype=torch.float32),
        torch.tensor(train_labels, dtype=torch.long),
    )
    batches = DataLoader(dataset, batch_size=64, shuffle=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AvocadoClassifier(train.shape[1], 64, len(classes)).to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.00001)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(1, 11):
        model.train()
        total_loss = 0.0
        for values, labels in batches:
            values, labels = values.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(values), labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(values)
        print(f"Epoch {epoch}: loss {total_loss / len(dataset):.6f}")
    model.eval()
    with torch.no_grad():
        predicted = (
            model(torch.tensor(test, dtype=torch.float32, device=device))
            .argmax(dim=1)
            .cpu()
            .numpy()
        )
    print(f"Accuracy: {accuracy_score(test_labels, predicted):.4f}")


if __name__ == "__main__":
    main()
