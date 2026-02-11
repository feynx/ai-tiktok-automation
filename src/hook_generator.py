import random


HOOK_MAP = {

    "curiosity": [
        "What if {topic} changes everything?",
        "Have you noticed how {topic} is evolving?",
        "This might surprise you about {topic}.",
        "Here’s something interesting about {topic}.",
    ],

    "fear": [
        "Most people are ignoring the danger of {topic}.",
        "This mistake in {topic} could cost jobs.",
        "The dark side of {topic} is growing fast.",
    ],

    "educational": [
        "Let’s understand how {topic} really works.",
        "Here’s what you need to know about {topic}.",
        "This is how {topic} is changing industries.",
    ]

}


def generate_hook(topic, tone="curiosity"):

    templates = HOOK_MAP.get(tone, HOOK_MAP["curiosity"])

    template = rando
