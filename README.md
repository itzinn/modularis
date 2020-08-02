# Modularis

Wordlist Generator that uses target's informations.

Its operation is based on generational modules.


## Disclaimer

This repository is for education purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. 


## Installation

```bash
git clone https://github.com/itzinn/modularis.git
```


## Usage

```bash
python modularis.py [-h]
```


## Gerational Modules Description

### Mr Robot Module

  input: word1;word2;word3;word4...

  output: word1, word2, word3, word1word2, word1word2word3...

  **Example:**
  
<blockquote>
  
  _Enter keywords or alpha-numeric sequences separated by ';' :_ john;mary;freddy...
  
  
  _Generated Words:_ john, mary, freddy, johnmary, johnfreddy, johnmaryfreddy, maryjohn...

</blockquote>

### Dates Module

   input: year1/year2

   output: 0101year1, 0201year1 ... 3112year2

   **Example:**
   
<blockquote>
  
   _Enter the year range of the dates to be generated:_ 1980/2015
  
  
   _Generated Words:_ 01011980, 02011980, ..., 01011987, ..., 31122015
   
</blockquote>

### Password format Module

   input: <em>word</em>%@^,[123]
   
   output: word0a!1, word0a!2, ..., word9z=3

   **Example:**
   
<blockquote>
  
   _Enter the password format:_ pass%%%
  
  
   _Generated Words:_ pass000, pass001, pass002, ..., pass999
   
</blockquote>

### Informational Module

input: answers to the questions
   
output: several combinations based on the answers

### Incremental Module

   input: personal data + words lenght range
   
   output: all possibilites for the charset selected and the lenght range

   **Example:**
   
<blockquote>
  
   _Enter the length range of the passwords that will be generated:_ 5/8
  
  
   _Generated Words:_ aaaaa, aaaab, aaaac, ..., zzzzzzzz
   
</blockquote>


## Credits

https://github.com/UndeadSec/GoblinWordGenerator

