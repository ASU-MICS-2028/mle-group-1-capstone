---
summary: Feedforward, CNN, RNN, transformer, autoencoder and GAN suit different kinds of data.
type: concept
tags: [neural-networks, architectures]
sources: [neural networks slides, lecture-10 recording]
---
# Types of neural networks

Pick the architecture that matches the shape of your data.

- **Feedforward (MLP)**: data flows one way, no loops, no memory. For basic prediction and classification on tabular features.
- **Convolutional (CNN)**: for grid-like data such as images. A small window slides over the grid and learns local patterns (edges, textures). Used for image recognition, face detection, medical imaging.
- **Recurrent (RNN, including LSTM)**: for sequences where order matters (sentences, time series). Loops let the network "remember" earlier inputs. Used for language, speech, time-series prediction. Processes one step at a time.
- **Transformer**: uses **attention**, which works out how strongly each item in a sequence relates to every other item. Processes the whole sequence at once (in parallel). Now the state of the art for language models, translation and code generation.
- **Autoencoder**: an encoder squeezes the data into a compact representation; a decoder rebuilds it. Used for compression, anomaly detection (bad rebuild = unusual input) and denoising.
- **GAN** (generative adversarial network): two networks compete. A generator makes fake data; a discriminator tries to tell real from fake. Used to generate realistic images.

The lecturer's point: for every application, you have to understand the right network to use.

## For the capstone
Our data is a small table of region-week features, so the only fitting NN is a small feedforward MLP. An RNN over weekly sequences is out of scope for five weeks and our data size.

## Related
- [Neural network](neural-network.md)
- [Multilayer perceptron](multilayer-perceptron.md)
