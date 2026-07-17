[ WORKING DIRECTORY ] → git add ->  [ STAGING AREA ] → git commit → [ Commit Histore ]

* Repository - Project folder innitialize by git by doing git init we can track entire chnage history over time made to that folder.
             - It contains Author, timestamp and message per save.
             - Any previous version is restorable.

* Working Direectory - The folder in my computer which currentl anyone will be working on.
                     -   Ex:- etl_pipeline is called current working directory
                     - Anyupdation make to this folder will be tracked by git if mentioned to do so.

* Staging Area  -   It is the stage where we can review before doing actual permanet commit.
                -   It's used for let's say we have modified 3 files and may want to commit 2 of them together so to review which file we need to commit this area is   helpful for.
                - It helps in clear commit.

* Commit History - We can see the comit hitory by doing git log --oneline 
                 - This present the entire detail history of the chnages or modification done to a file.
                 - It's like a permanet record can't be deleted

* Local Repository  - The version control tool that lives in own computer which works locally without internet.
                    - Where entire project history lives in.
                    - Works offline
                    - it stores the git history locally keeping track of changes made.
                    - It does not depend on GitHub.
                    - Git is an example.

* Remote Repository - Copy of repository hosted on GitHub.
                    - It's a collaborative version of the project.
                    - Local work pushed here for review and merging.
                    - GitHub
