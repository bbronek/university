import pandas as pd


def main():
    titanic_data = pd.read_csv('titanic.tsv', sep='\t')

    print("Before change:")
    print(titanic_data["Sex"][100:130])
    print(titanic_data["Embarked"][100:130])

    titanic_data["Sex"] = titanic_data["Sex"].map({'male': 0, 'female': 1})
    titanic_data["Embarked"] = titanic_data["Embarked"].map({'S': 0, 'C': 1, 'Q': 2})

    titanic_data["Sex"] = pd.to_numeric(titanic_data["Sex"], errors="coerce")
    titanic_data["Embarked"] = pd.to_numeric(titanic_data["Embarked"], errors="coerce")

    print("\n After change:")
    print(titanic_data["Sex"][100:130])
    print(titanic_data["Embarked"][100:130])
    
if __name__ == "__main__":
    main()