import os

print("1. Preprocess MIDI")
print("2. Train Model")
print("3. Generate Music")

choice = input("Select Option: ")

if choice == "1":
    os.system("python src/preprocess.py")

elif choice == "2":
    os.system("python src/train.py")

elif choice == "3":
    os.system("python src/generate.py")

else:
    print("Invalid Option")