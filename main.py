def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
once upon a time, there was a {noun1} who loved to {verb1} all day.
one day, {noun2} walked into the room and caught the {noun1} in the act.

{noun2}: "what are you doing?"
{noun1}: "I'm just {verb1}ing, what's the big deal?"
{noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "Same here. It’s been non-stop at work lately. I was thinking about grabbing lunch together tomorrow. Interested?"
{noun2}: "That sounds great! I’d love to catch up. Do you have a place in mind?"
{noun1}: "How about that new café downtown? I’ve heard they have a pretty good menu."
{noun2}: "I’ve heard good things about it too. Let’s do it. What time works for you?"
{noun1}: "How about 12:30 PM? That should give us enough time to avoid the lunch rush."
{noun2}: "Perfect. I’ll see you there at 12:30 then. Looking forward to it!"
{noun1}: "Me too! See you tomorrow, {noun2}. "
{noun2}: "See you, {noun1}!"


"""
print(story)
