
# Midori AI Subsystem: Streamlining AI Workloads

![Midori AI photo](https://tea-cup.midori-ai.xyz/download/logosubsystem.png)

The ``Midori AI Subsystem`` offers an innovative solution for managing AI workloads through its advanced integration with containerization technologies. Leveraging the lightweight and efficient design of [PixelArch OS](https://io.midori-ai.xyz/pixelos/), this system empowers developers, researchers, and hobbyists test AI systems effortlessly across a variety of environments.

At the heart of the Midori AI Subsystem is [PixelArch OS](https://io.midori-ai.xyz/pixelos/), a custom Arch Linux-based operating system optimized for containerized workloads. It provides a lightweight, streamlined environment tailored for modern AI development. 

* Simplified Deployment: Deploy AI systems effortlessly with pre-configured or built-on-request container images tailored to your needs.
* Platform Versatility: Supports Docker, Podman, LXC, and other systems, allowing you to choose the best fit for your infrastructure.
* Seamless Experimentation: Experiment with various AI tools and models in isolated environments without worrying about conflicts or resource constraints.
* Effortless Scalability: Scale AI workloads efficiently by leveraging containerization technologies.
* Standardized Configurations: Reduce guesswork with standardized setups for AI programs.
* Unleash Creativity: Focus on innovating and developing AI solutions while the Subsystem handles system configuration and compatibility.

## ----- Install / Setup -----

- [Midori AI Subsystem Install Page](https://io.midori-ai.xyz/subsystem/manager/)

- Build it yourself steps below

### Prerequisites
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [UV](https://docs.astral.sh/uv/getting-started/installation/)

- **System requirements**:
  - OS: Windows, macOS, or Linux
  - Python: None, Use ``UV``
  - Minimum RAM: 10GBs
  - Disk space: 25GBs to 550GBs

- **Dependencies**:
  - ``UV`` auto installs all dependencies and python into a venv for you
  - ``containdred`` system lets each of the backends run in a docker api friendly system

To run the subsystem manager yourself
```bash
uv run main.py
```

## ----- Installable Backends -----

### Chat UIs
Chat with your own locally hosted AI, via:
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - For chating with your docs using LocalAI or other LLM hosts
- [Big-AGI](https://github.com/enricoros/big-AGI) - For chating with your docs using LocalAI or other LLM hosts

### LLM Backends
Seamlessly integrate your AI systems with these LLM Backends:
- [LocalAI](https://github.com/mudler/LocalAI) - For LLM inference, Embedding, and more
- [Ollama](https://github.com/ollama/ollama) - For LLM inference, Embedding, and more
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) - For training your own fine tuned LLMs

### LLM Hubs
Chat with these locally hosted LLM Hubs, using the LLM backends in the Subsystem:
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - For Setting up / running LLM "Experts"
- [MemGPT](https://github.com/cpacker/MemGPT) - For Setting up / running LLM with OS like memory
- [Elroy](https://github.com/elroy-bot/elroy) - For Setting up / running LLM "Personas" with memory

### Cluster Based AI
Support the Midori AI node based cluster system!
- Midori Ai Cluster - Not Ready Yet

### Image AI
Make photos for your AI's, by using:
- [InvokeAI](https://github.com/invoke-ai/InvokeAI) - For making photos using AI models

## Get Involved:

* **Join our Discord community:** https://discord.gg/xdgCx3VyHU
* **Connect with us on Facebook:** https://www.facebook.com/TWLunagreen
* **Follow us on Twitter:** https://twitter.com/lunamidori5
* **Explore our Pinterest boards:** https://www.pinterest.com/luna_midori5/
* **Follow us on Twitch:** https://www.twitch.tv/luna_midori5
* **Subscribe to our YouTube channel:** https://www.youtube.com/channel/UCVQo4TxFJEoE5kccScY-xow
* **Support us on PayPal:** https://paypal.me/midoricookieclub?country.x=US&locale.x=en_US

**Unleashing the Future of AI, Together.**