from django.shortcuts import redirect, render

from .blockchain import VotingBlockchain

CANDIDATES = ["Candidate A", "Candidate B", "Candidate C"]

# One in-memory chain per server process (resets on restart).
blockchain = VotingBlockchain()


def vote(request):
    if request.method == "POST":
        candidate = request.POST.get("candidate_name")
        if candidate in CANDIDATES:
            blockchain.add_vote(candidate)
        return redirect("results")
    return render(request, "voting/vote.html", {"candidates": CANDIDATES})


def results(request):
    tally = {name: 0 for name in CANDIDATES}
    for block in blockchain.chain[1:]:
        tally[block.candidate_name] = tally.get(block.candidate_name, 0) + 1
    return render(
        request,
        "voting/results.html",
        {
            "blockchain": blockchain.chain,
            "tally": tally,
            "chain_valid": blockchain.is_chain_valid(),
        },
    )
