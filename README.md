# Lab 10 - Problem-Solving Practice 2

More **LeetCode / ICPC-style problems**, a notch harder than last week. Most of these
have a clean solution built on a **stack** or a **queue** - the data structures from
this week's lectures. As before, the real goal is the whole loop from *problem* to
*plan* to *working code*.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 10 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

You should be a member of the **CSCI1030U** organization on GitHub, from the invitation
sent out after Lab 01. If you never accepted that invitation, do it now (check your email,
or go to <https://github.com/CSCI1030U>) - you can't create your lab repository until
you're a member. Tell your lab instructor if no invitation ever arrived.

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 10 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** `CSCI1030U` (the organization, *not* your own account)
   - **Repository name:** `lab10-your-username` - for example `lab10-jsmith2026`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab10-your-username
cd lab10-your-username
```

## How to approach each problem

These are harder, so the outline matters even more. Before writing (or generating) any
code:

1. **Restate** the problem in your own words.
2. **Try a small example by hand** - and notice *how* you did it. (For several of these,
   watching what you push and pop is the whole trick.)
3. **Sketch the approach** - which data structure fits, and what are the steps?

Each function in `lab10.py` has an `# Outline` comment - jot your plan there first, then
turn it into code (you may use an AI assistant to help - see **Using AI**).

## Problems

Edit **`lab10.py`**. Don't rename the functions - the tests use these names.

### Part 1 - `eval_rpn(tokens)`

`tokens` is a list of strings in **Reverse Polish Notation** (postfix): each token is
either an integer or one of `"+"`, `"-"`, `"*"`, `"/"`. Evaluate the expression and
return the integer result. Division truncates toward zero (`int(a / b)`).

```python
eval_rpn(["2", "1", "+", "3", "*"])    # returns 9    ((2 + 1) * 3)
eval_rpn(["4", "13", "5", "/", "+"])   # returns 6    (4 + 13 // 5)
```

Hint: push numbers onto a stack; on an operator, pop the top two, combine them, and push
the result back.

### Part 2 - `decode_string(s)`

Decode a string that uses the rule `k[encoded]`, meaning `encoded` repeated `k` times.
The brackets can be **nested**.

```python
decode_string("3[a]2[bc]")   # returns "aaabcbc"
decode_string("3[a2[c]]")    # returns "accaccacc"
```

Hint: a stack lets you remember the text and the repeat-count from *outside* each `[`
while you work on what's inside.

### Part 3 - `daily_temperatures(temps)`

`temps` is a list of daily temperatures. For each day, return **how many days you'd wait
for a warmer temperature**; put `0` if no warmer day ever comes.

```python
daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])   # returns [1, 1, 4, 2, 1, 1, 0, 0]
daily_temperatures([30, 40, 50, 60])                   # returns [1, 1, 1, 0]
```

Hint: keep a stack of days that are still *waiting* for a warmer one.

### Part 4 - `num_islands(grid)`  *(stretch - optional)*

`grid` is a list of equal-length strings made of `"1"` (land) and `"0"` (water). Count
the **islands** - groups of `"1"`s connected up/down/left/right (not diagonally).

```python
num_islands(["11000", "11000", "00100", "00011"])   # returns 3
num_islands(["11110", "11010", "11000", "00000"])   # returns 1
```

Hint: when you find an unvisited `"1"`, explore outward from it (a stack or queue of
cells to visit works well), marking every connected cell so you don't count it twice.

This part is optional - the three problems above are the core of the lab.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

Read the output closely - a failing test shows the input, what it expected, and what
your code returned. Fix, save, and run `pytest` again.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 10 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 10 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab10-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You **may use an AI assistant to help you write the code** for this lab. Build the habit
first, though: **work out the problem-solving outline yourself before you involve the
AI.** Restate the problem, try a small example by hand, and decide which data structure
fits - *then* lean on the AI to help turn that plan into Python. Let the AI do the
implementing, not the thinking.

Use a free model, and be ready to **explain and modify** any code you submit - the lab
instructor may ask you to walk through it or change how it works.
