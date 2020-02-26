import wolframalpha

userIn = input("Question: ")

app_id = "LQEGLQ-JVJTQP73QA"

client = wolframalpha.Client(app_id)

result = client.query(userIn)

answer = next(result.results).text
print(answer)

