import matplotlib.pyplot as plt
subjects=["python","c","java","c++"]
scores=[88,92,79,85]
plt.bar(subjects,scores,color="red")
plt.title("student performance")
plt.xlabel("subjects")
plt.ylabel("Marks")
plt.show()