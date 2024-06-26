# 40kHammerOfMath

The start of a tool for calculating rolls in 10th edition 40k

## Usage

The current version of main.py will output to a CSV and create a crude Sankey diagram.

## Running

1. pip install -r requirements.txt
2. run main.py
3. You can define your own units in units.py and give them weapons that you build in weapons.py
4. Use a feel no pain value of 7 if you aren't using it. Same for invulns
5. Build your attacker list like so: `attacker_list: list[list[tuple[Unit, int]]]`. This is done because you can have several different attackers at once all attacking one defender. The Unit, int tuple is the Unit class and a count of bodies. This is particularly useful if you have mixed weapons in the squad since you'll be using multiple unit types.
6. Build your defender list like `[teq, meq]`
7. The CSV output will apply every set of attackers against every defender. Don't start adding loads here unless you want long run times - it's quadratic scaling.

## TODO

- [ ] Add support for rerolls
- [ ] Add support for modifiers
- [x] Add support for weapon and unit traits (needs refactor to be callable)
- [ ] Make a version that can calculate averages (but retain some actual rolling for one-off uses)
- [x] Move away from lists to numpy arrays
- [ ] Start on a web app version?
- [x] Display Sankey diagrams (kinda)
- [x] Possible refactor for scenario? Unsure yet (kind of...)

## Example Output to Console

Somewhat outdated now. Current version of main.py will output some stuff for you.
The Scenario class is still a bit of a mess but contains everything you need.

```commandline
Starting Simulation!

------------Attackers-------------
Allarus Custodians with Guardian Spears (Melee) x3 with Guardian Spear Melee
Total Attacks: 21
To Hit: 2+
Strength: 5
AP: -2
Damage: 2

------------Defender-------------
Ork Boyz with Choppas (Melee) x20
Toughness: 5
Save: 5+
Invuln: 5+
FNP: 5+
Wounds per model: 1 (20 Total)

-----------------Hits-----------------
Rolls: [5, 6, 6, 6, 3, 6, 5, 5, 6, 4, 1, 6, 1, 2, 6, 5, 5, 2, 6, 5, 3],
Attempts: 21,
Successes: 19,
Failures: 2,
One Rolls: 2,
Crit Rolls: 8,
Final Rolls: [5, 6, 6, 6, 3, 6, 5, 5, 6, 4, 1, 6, 1, 2, 6, 5, 5, 2, 6, 5, 3]

-----------------Wounds-----------------
Rolls: [5, 1, 2, 3, 6, 4, 5, 3, 5, 1, 2, 3, 4, 2, 6, 5, 4, 5, 6],
Attempts: 19,
Successes: 11,
Failures: 8,
One Rolls: 2,
Crit Rolls: 3,
Final Rolls: [5, 1, 2, 3, 6, 4, 5, 3, 5, 1, 2, 3, 4, 2, 6, 5, 4, 5, 6]

-----------------Saves-----------------
Rolls: [4, 4, 6, 3, 2, 3, 1, 5, 1, 1, 1],
Attempts: 11,
Successes: 2,
Failures: 9,
One Rolls: 4,
Crit Rolls: 1,
Final Rolls: [4, 4, 6, 3, 2, 3, 1, 5, 1, 1, 1]

-----------------FNP-----------------
Rolls: [2, 6, 1, 4, 3, 1, 5, 2, 4, 6, 5, 5, 1, 5, 2, 5, 2, 2],
Attempts: 18,
Successes: 7,
Failures: 11,
One Rolls: 3,
Crit Rolls: 2,
Final Rolls: [2, 6, 1, 4, 3, 1, 5, 2, 4, 6, 5, 5, 1, 5, 2, 5, 2, 2]

-----------------Wound Damage List-----------------
[2, 2, 2, 2, 2, 1]

-----------------Results----------------
Scenario: [(Allarus Custodians with Guardian Spears (Melee), 3)] vs (Ork Boyz with Choppas (Melee), 20)
Total Attacks: 21
Total Hits: 19
Total Wounds: 11
Total Unsaved Saves: 9
Total Damage Dealt: 11 over 6 wounds
Total Not FNP: 11
Defender Models Killed: 6


Process finished with exit code 0
```
