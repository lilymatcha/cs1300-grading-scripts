# cs1300-grading-scripts

Grading scripts for CS1300 at Brown University.

## First, a strong warning

TL;DR Don't ever publish student info online.

Should you choose to contribute to this repository (good on you!), please triple-check before pushing any code to Github (or any other hosting service) that you haven't accidentally included any student info, either from running the script locally or from testing your changes. You can make use of the `.gitignore` for this, or just do it manually by keeping your "public" script work in a separate file location from your "in-use" script work.

## How to assign grading to TAs

### Before you start

1. Ensure you have Python 3 installed.
2. Make sure the TAs have filled out their blocklists and that you have stored them in `ta_blocklists/`.

#### Tips and things worth noting

* Blocklists should be separate files because they are private information. TAs shouldn't be able to view one another's blocklists.

### Running `assign_graders_to_students.py`

1. Navigate to `scripts/` and open `assign_graders_to_students.py`.
2. update the values on lines 4-6.
3. Run `python assign_graders_to_students.py`. Should you get a warning saying that not all students have been assigned to graders, first try running the script again. If that doesn't work, just manually assign the students in the completed file. (This error tends to come up if a TA with a long blocklist happens to be the last in queue to get handins assigned to them.)
4. Give the TAs their assignments, preferably over email (make sure the subject line is descriptive so they can easily search for it later). Make sure you do this before grading meeting so that no one is waiting on you.

#### Tips and tricks

* You might be tempted to make a CSV with everyone's assignments. I recommend against this. There is sometimes variance in how many assignments each TA has, and you don't want to them to start wondering "Why did I get more than this other TA?" The variance is rarely more than one or two handins, but still, this is something to keep in mind.
* Consider making a Google Form where TAs can mark down if they're done with grading or not. I recommend a Google Form over a Google Sheet because it's a bit easier for the TAs.
* Set up a script that automatically sends the Google Form to TAs the day before grading is due to ask if they're done, and if not, when they will be done. Set the options for when they'll be done to just one or two days, and say that if they need more time than that, they must contact the HTAs. This will save you a lot of headaches from hunting down TAs who haven't finished their work, or wondering if they're done. You'll have all the info you need all in a single spreadsheet.
* You'll notice that in `assign_grading()` we shuffle the list of TA names. This is to avoid bias by making sure that TAs aren't assigned to the same batch of students too many times. We don't shuffle the list of handins, because that way TAs don't have to jump around the list of students on Speedgrader, which can be a semi-annoying process. (We want to minimize TA frustration regarding grading as much as possible.)