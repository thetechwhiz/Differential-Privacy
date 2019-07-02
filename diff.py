import torch


def get_paralleldb(db,remove_index):

    return torch.cat((db[0:remove_index],db[remove_index+1:]))

def get_paralleldbs(db):

    parallel_dbs = list()

    for i in range(len(db)):
        pdb = get_paralleldb(db,i)
        parallel_dbs.append(pdb)

    return parallel_dbs
def create_db_and_parallels(num_entries):

    db = torch.rand(num_entries)>0.5
    pdbs=get_paralleldbs(db)

    return db,pdbs



def sensitivity(query,n_entries=1000):
    db, pdbs = create_db_and_parallels(n_entries)

    full_db_result = query(db)

    max_distance=0
    for pdb in pdbs:
        pdb_result=query(pdb)

        db_distance = torch.abs(pdb_result - full_db_result)
        if(db_distance > max_distance):
            max_distance=db_distance

    return max_distance


def query(db,threshold=5):
    return (db.sum()>threshold).float()

for i in range(10):
    sens_f=sensitivity(query,n_entries=10)
    print(sens_f)






