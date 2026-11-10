scores = [45, 78, 91, 53, 60, 39, 88, 75] 
passed = 0
failed = 0
for score in scores:
    if score >= 60:
        passed = passed + 1
    else:
        failed = failed + 1

print("Зачет:", passed)
print("Незачет:", failed)
