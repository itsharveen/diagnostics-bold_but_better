""" Python script to validate data

Run as:

    python3 scripts/validate_data.py data
"""

from pathlib import Path
import sys
import hashlib
import glob2 as glob


def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    file = Path(filename).read_bytes()
    # Calculate, return SHA1 has on the bytes from the file.
    return hashlib.sha1(file).hexdigest()

def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    # Read lines from ``data_hashes.txt`` file.
    # Split into SHA1 hash and filename
    # Calculate actual hash for given filename.
    # If hash for filename is not the same as the one in the file, raise
    # ValueError
    # This is a placeholder, replace it to write your solution.
    local_path = Path(data_directory)
    hashes = glob.glob(str(local_path) + "/*" + "/data_hashes.txt")
    lines = hashes.read_text().splitlines()
    for line in lines:
        hash, filename = line.split()
        filename_path = (str(local_path) + filename)
        hash_act = file_hash(filename_path)
        if hash_act != hash:
            raise ValueError(f'Hash for {filename} is {hash_act}, which does not match the expected {hash}')


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
