>> > q = Question.objects.get(pk=1)
Traceback(most recent call last):
    File "<console>", line 1, in <module >
NameError: name 'Question' is not defined
>> > from polls.models import Choice, Question
>> > from django.utils import timezone
>> > q = Question.objects.get(pk=1)
>> > q.was_published_recently()
False
>> > q.choice_set.all()
<QuerySet[] >
>> > q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much >
>> >
KeyboardInterrupt
>> >
>> >
KeyboardInterrupt
>> > q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky >
>> > c.question
Traceback(most recent call last):
    File "<console>", line 1, in <module >
NameError: name 'c' is not defined
>> > c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>> > c.question
<Question: That's hot >
>> > q.choice_set.all()
<QuerySet [ < Choice: Not much > , < Choice: The sky > , < Choice: Just hacking again > ] >
>> > q.choice_set.count()
3
>> > Choice.objects.filter(question__pub_date__year=current_year)
Traceback(most recent call last):
    File "<console>", line 1, in <module >
NameError: name 'current_year' is not defined
>> > Choice.objects.filter(question__pub_date__year=2021)
<QuerySet [ < Choice: Not much > , < Choice: The sky > , < Choice: Just hacking again > ] >
>> > q.choice_set.filter(choice_text__startswith='Just hacking')
<QuerySet [ < Choice: Just hacking again > ] >
>> > c.delete()
(1, {'polls.Choice': 1})
>> >
