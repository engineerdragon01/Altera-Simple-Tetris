# Adam's Solution for Altera's Simple Tetris Problem

## Instructions
- Clone this repository to your local machine:
- > git clone https://github.com/engineerdragon01/Altera-Simple-Tetris.git
- If you haven't already, please download Conda via Anaconda or miniconda command line installer (I used Anaconda)
- > [Anaconda Command Line Install](https://docs.anaconda.com/anaconda/install/mac-os/)
- Once you have successfully downloaded Anaconda or miniconda and, as a result, installed conda, you should notice that your terminal with your base environment activated will look something like this:
```
(base) engineerdragon01@Adams-MacBook-Pro ~ % ls
Applications	Documents	Library		Music		Public		mysqlbackup.sql
Desktop		Downloads	Movies		Pictures	anaconda3
```
- Please navigate to the git repository in your terminal
- Then, please create a new environment in the same directory using the following command:
```
(base) engineerdragon01@Adams-MacBook-Pro Altera-Simple-Tetris % conda create --name SimpleTetris
Channels:
 - defaults
Platform: osx-arm64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/engineerdragon01/anaconda3/envs/SimpleTetris



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate SimpleTetris
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
- Activate the new environment
```
(base) engineerdragon01@Adams-MacBook-Pro Altera-Simple-Tetris % conda activate SimpleTetris
(SimpleTetris) engineerdragon01@Adams-MacBook-Pro Altera-Simple-Tetris %
```
> NOTE: There is no major necessity here for using a conda environment, but to isolate your environments in your local machine to run this project, this may help
> We will be using the latest 3.9 version of python as that is the default installed and we require no unique python nuances from previous versions
- To run the `tetris.py` file you can  use the following command: `python3 tetris.py < input.txt > output.txt`

## Implementation
The logic for my approach to this problem is a bit brute-force, but the workflow happen like so:
- Process raw text from input.txt
- Iterate through each line (which represents a "game")
  - Iterate through each "move" (i.e. "Q1") in the "game"
    - Drop the piece from the top of the grid
      - Determine valid placement and place the piece at it's lowest valid placement (growing the height of the grid if necessary)
    - Adjusting the grid accordingly if any full rows occur
  - Output the maximum height of the game
- Once all the "games" have been executed and the maximum heights are all outputted, we have finished playing Simple Tetris
