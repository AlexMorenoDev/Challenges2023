"""
 * Crea un programa que lea los últimos 10 commits de este repositorio (https://github.com/mouredev/retos-programacion-2023)
 * y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
"""
import time
from git import Repo

def main():
    repo_folder = "./repo"
    try:
        repo = Repo.clone_from("https://github.com/mouredev/retos-programacion-2023", repo_folder, branch="main")
    except:
        repo = Repo(repo_folder)
    
    
    last_commits = list(repo.iter_commits("main", max_count=10))
    
    i = 1
    for commit in last_commits:
        message = commit.message.replace("\n", " ")
        committed_date = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(commit.committed_date))
        print(f"Commit {i} | {commit.hexsha} | {commit.author} | {message} | {committed_date}")
        i += 1

if __name__ == "__main__":
    main()

