# foundation
This is a simple pipeline setup based on rez

#Setup - Step 1
Install rez add rez packages path to your environment variable, I have simple setup here if people like to take a reference
https://github.com/cgarjun/pipesource/blob/master/bin/initialize_pipeline

Setup - Step 2

clone the foundation packege and rez-release the foundation package.

Setup - Step 3

Below is the simple example of file structure I have been using
```bash
├── dev
│   ├── foundation
│   └── pipesource
├── projects
└── software
    └── rez (actual rez software)
    └── config (facility level configs)
    └── internal (rez packages)
    └── external (rez packages)
    └── suites (facility level rez suites)
         └── 0.0.1 (version)
         └── 0.1.2 (version)
         └── current (symlink to version)
```

Once you have structure 
## CLI
CLI usages and examples
#### suite_gen examples
Create a new suite and add all profiles
```python
suite_create /Users/arjun/nirvana/software/suites/ 0001 --create
```

Release a suite
```python
suite_create /Users/arjun/nirvana/software/suites/ 0001 --release
```

#### profile_gen example

Generate a selection profile
```python
profile_create /Users/arjun/nirvana/software/suites/ 0001 foundation
```

#### project_gen example

Creates a projects basic directory structures

```python
project_gen dummy
```
 