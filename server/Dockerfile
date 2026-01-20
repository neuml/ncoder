# Set base image
ARG BASE_IMAGE=neuml/txtai-gpu
FROM $BASE_IMAGE

# Copy files
COPY *.yml start.sh .

# Environment parameters
ENV CONFIG="opencode.yml"

RUN \
    # Install required packages
    apt-get update && \
    apt-get -y --no-install-recommends install curl git && \
    rm -rf /var/lib/apt/lists && \
    chmod +x /app/start.sh && \
    \
    # Install OpenCode
    curl -fsSL https://opencode.ai/install | bash && \
    ln -s ~/.opencode/bin/opencode /app/opencode && \
    \
    # Install llama-cpp-python with GPU support, latest txtai from GH and other dependencies
    python -m pip install llama-cpp-python --force-reinstall --no-deps --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124 && \
    python -m pip install git+https://github.com/neuml/txtai && \
    python -m pip install markdownify && \
    \
    # Cleanup build packages
    apt-get -y autoremove

# Start server and listen on all interfaces
CMD ["/app/start.sh"]
