from django.test import SimpleTestCase

from .blockchain import VotingBlockchain


class BlockchainTests(SimpleTestCase):
    def test_new_chain_is_valid(self):
        chain = VotingBlockchain()
        chain.add_vote("Candidate A")
        chain.add_vote("Candidate B")
        self.assertTrue(chain.is_chain_valid())

    def test_tampered_vote_is_detected(self):
        chain = VotingBlockchain()
        chain.add_vote("Candidate A")
        chain.add_vote("Candidate B")
        chain.chain[1].candidate_name = "Candidate C"
        self.assertFalse(chain.is_chain_valid())

    def test_vote_flow(self):
        response = self.client.post("/vote/", {"candidate_name": "Candidate A"})
        self.assertEqual(response.status_code, 302)
        page = self.client.get("/results/")
        self.assertContains(page, "verified")
        self.assertContains(page, "Candidate A")
