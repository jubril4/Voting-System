# Blockchain Voting System

Senior Design project (Capitol Technology University, 2023 to 2024): a tamper evident voting ledger with a Django web interface.

## How it works
- Each vote is stored as a block containing a timestamp, the candidate, its own SHA-256 hash, and the hash of the previous block.
- Because every hash depends on the block before it, changing any recorded vote breaks the chain.
- `is_chain_valid()` recomputes every hash and link, and the results page reports whether the ledger is intact.

## Run it
```bash
pip install -r requirements.txt
python manage.py runserver
```
Open http://127.0.0.1:8000, cast votes, then view the ledger and tally on the Results page.

```bash
python manage.py test      # chain validity, tamper detection, and vote flow tests
python standalone_demo.py  # command line demo of the blockchain on its own
```

## Project structure
| Path | Purpose |
|---|---|
| `voting/blockchain.py` | `VoteBlock` and `VotingBlockchain` classes |
| `voting/views.py` | Vote and Results views |
| `voting/templates/voting/` | Page templates |
| `voting/tests.py` | Automated tests |
| `standalone_demo.py` | Command line version |

## Notes
The chain is held in memory, so it resets when the server restarts. For a production system, the next steps would be persistent storage, voter authentication, and distributing the ledger across nodes.
