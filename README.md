# Expected functionality of pachyderm incremental feature

### Notation
- Repos: All the repos are represented by capital letters, such as `A`, `B`, etc
- Pipelines: All the pipelines are represented by small letters. For example, `p`, `q`, etc.
- Datum: particular datum of a repo `A` are reprented by `A[path/to/datum]`
- Cross Inputs: A pipeline `p` which takes crossed inputs are from repo `A` and `B` are represented as `p(A, B)`
- Output repo: if `P = p(A, B)`, this means that `P` is the output repository of the pipeline `p`.
- Commit: a particular commit in repo `A` is represented like `A{commit-id}`
  - For convenience, we will assign commits as sequential natural number, for example, `A{1}`, `A{2}`, etc.

## Example
- Consider a simple DAG: `p->q->r` defined by following pipelines
  - `P = p(C[p_config.txt], D[/])`
  - `Q = q(C[q_config.txt], P[/])`
  - `R = r(C[r_config.txt], Q[/])`
 
Where 
 - `C` is the configuration repo that modifies the behaviour of pipeline.
    - `p_config.txt` is the configuration file for pipeline `P`
    - same for `q` and `r` pipelines.
 - `D` is the input data that is processed through the DAG.
 
 
## Use case
- Commit all the data
  - `commit(D, input.json)`
  
- Commit all the config 
  - `commit(C, p_config.txt, q_config.txt, r_config.txt)`
  
- Deploy all the pipelines
  - start-pipeline(p)
    - Job: `P{1}[/] = p(C{1}[p_config.txt], D{1}[/])`
  - start-pipeline(q)
    - Job: `Q{1} = q(C(1)[q_config.txt], P{1}[/])`
  - start-pipeline(r)
    - JOb: `R{1} = r(C{1}[r_config.txt], Q{1}[/])`
    
- Modify `q_config.txt`, should trigger following jobs
  - Job: `Q{2} = q(C{1}[q_config.txt], P{1}[/])`
  - Job: `R{2} = r(C{2}[r_config.txt], Q{2}[/])`
