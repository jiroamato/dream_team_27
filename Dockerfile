FROM condaforge/miniforge3:25.9.1-0

COPY conda-lock.yml /tmp/conda-lock.yml

RUN conda install -c conda-forge conda-lock=3.0.4 -y \
    && conda-lock install -n student-grade-predictor /tmp/conda-lock.yml \
    && conda clean --all -y -f

ENV PATH="/opt/conda/envs/student-grade-predictor/bin:$PATH"

RUN quarto install tinytex --no-prompt

SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /workplace

EXPOSE 8888

CMD ["/opt/conda/envs/student-grade-predictor/bin/jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--IdentityProvider.token=''", "--ServerApp.password=''"]