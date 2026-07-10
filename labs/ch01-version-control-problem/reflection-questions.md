1. Which file is latest?
#### Ans:
* Seems the customer_cleaning_final_v2.py can be the final one yet it's hard to detect without git tracking.
* To predict which one is the latest one we have to reley on our instinct that may be this is what should be the latest one.
* With git this guessing no need to be done

2. Which file is production-ready?

#### Ans:
* None of then seems production ready as far I understood a file must have some naming convention like customer_cleaning_date if it's done without git but yet if team is modifying in a day it's hard to recognize without git as we can't say by looking at those file what changed and when and is the change is relevant or not if not once overwritten the previous file is gone which is now impossible to get back without git.

3. What risk does this create?

#### Ans:
* This will create the problem of trust my file issue without git there is no record of what chnaged , who chnaged and when chnaged and if two or multiple team-mates are working on same file then without git it's hard to have a track on the actual file which is correct over so many people's working on same file who chnage what and when seems near to impossible to track and if accidentally overwritten and this casue issue in pipeline then that's another nightmare.

4. How would version control reduce these risks?

#### Ans:
* With version control systems like git in our local folder we can have track of our file with all modification information intaced into it.
* Git tell what modification occured, when occured, and who commited it.
* We can track our file easily with git 
* This creates no confusion over which file is latest.