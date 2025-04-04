# jupyter_integration.py
from IPython.core.magic import register_line_cell_magic
from coding_agent import coding_agent

def init_jupyter():
    @register_line_cell_magic
    def agent(line, cell=None):
        """Magic command for CodeAgent integration"""
        if cell is None:  # Line magic
            return coding_agent.run(line)
        else:  # Cell magic
            return coding_agent.run(f"{line}: {cell}")
    
    print("Jupyter magic commands registered!")
