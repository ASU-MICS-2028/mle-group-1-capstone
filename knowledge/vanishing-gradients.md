---
summary: In deep networks, gradients multiplied through many layers can shrink toward zero, so early layers stop learning.
type: concept
tags: [neural-networks, training, lecturer-emphasis]
sources: [lecture-11 recording]
---
# Vanishing gradients

Backpropagation multiplies many local derivatives together, one per layer. If those factors are small (less than 1), the product shrinks fast. Example: ten layers each contributing 0.25 gives 0.25¹⁰ ≈ 0.000001.

Result: the layers near the input get almost no gradient. Their weights barely change, so they barely learn. The deeper the network, the worse this gets.

The sigmoid makes it worse: its slope is at most 0.25, and almost zero for large positive or negative inputs. ReLU has slope 1 for positive inputs, which is one reason it is the usual hidden-layer choice.

The lecturer listed this as one cost of adding depth, and mentioned he asked about it in student interviews. Expect it as a question.

(The transcript renders the term as "vanishing radius"; it means vanishing gradients.)

## For the capstone
Not a risk for us: any NN we try will be one or two small layers.

## Related
- [Network depth and width](network-depth-and-width.md)
- [Chain rule in backpropagation](chain-rule-in-backpropagation.md)
- [Activation functions](activation-functions.md)
