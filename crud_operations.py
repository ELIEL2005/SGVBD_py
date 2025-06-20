from typing import List, Dict, Optional, Any

# AUTO-INCREMENTATION DE L'ID
def generate_id(table: List[Dict[str, Any]]) -> int:
    if not table:
        return 1
    return max(record["id"] for record in table) + 1

# CREER
def add_record(table: List[Dict[str, Any]], record: Dict[str, Any]) -> Dict[str, Any]:
    new_id = generate_id(table)
    record["id"] = new_id
    table.append(record)
    return record

# LIRE (par ID)
def get_record_by_id(table: List[Dict[str, Any]], record_id: int) -> Optional[Dict[str, Any]]:
    for record in table:
        if record["id"] == record_id:
            return record
    return None

# LIRE (balayage complet)
def get_all_records(table: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return table

# MISE A JOUR
def update_record(table: List[Dict[str, Any]], record_id: int, updated_data: Dict[str, Any]) -> bool:
    for record in table:
        if record["id"] == record_id:
            record.update(updated_data)
            record["id"] = record_id  # Ne pas modifier l’ID
            return True
    return False

# SUPPRIMER
def delete_record(table: List[Dict[str, Any]], record_id: int) -> bool:
    for i, record in enumerate(table):
        if record["id"] == record_id:
            del table[i]
            return True
    return False
