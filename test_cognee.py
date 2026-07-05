"""
test_cognee.py — the very first thing to run before building anything else.

Goal: prove that remember() -> recall() actually works with your chosen
free LLM provider. If this script works, Day 1's riskiest part is done.

Run with:  python test_cognee.py
"""

import asyncio
from dotenv import load_dotenv

# Load variables from .env into the environment BEFORE importing cognee,
# since cognee reads provider config at import/config time.
load_dotenv()

import cognee


async def main():
    print("1) Storing a fact into memory with remember()...")
    await cognee.remember(
        "The mitochondria is the powerhouse of the cell. "
        "It generates most of the cell's supply of ATP, used as a source of chemical energy."
    )
    print("   Done.\n")

    print("2) Asking a question with recall()...")
    results = await cognee.recall("What does the mitochondria do?")
    print("   Result(s):")
    for r in results:
        print("   -", r)

    print("\nIf you see a relevant answer above, your setup works. Onward!")


if __name__ == "__main__":
    asyncio.run(main())
