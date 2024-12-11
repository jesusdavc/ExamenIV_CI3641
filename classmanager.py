class ClassManager:
    def __init__(self):
        self.classes = {}

    def define_class(self, class_definition):
        """
        Define una CLASS 
        String con el formato format CLASS <tipo> [<nombre>]
        
        """
        parts = class_definition.split()
        if len(parts) < 2 or parts[0] != "CLASS":
            raise ValueError("Defición de CLASS invalida")

        class_name = parts[1]

        # Check para herencia
        if ":" in parts:
            superclass_index = parts.index(":") + 1
            superclass_name = parts[superclass_index]
            methods = parts[superclass_index + 1:]
        else:
            superclass_name = None
            methods = parts[2:]

        if class_name in self.classes:
            raise ValueError(f"Class '{class_name}' ya existe")

        if superclass_name and superclass_name not in self.classes:
            raise ValueError(f"Superclass '{superclass_name}' no existe")

        if superclass_name:
            # Check para ciclos de herencia
            current = superclass_name
            while current:
                if current == class_name:
                    raise ValueError("Ciclo de herencia detectado")
                current = self.classes[current].get("superclass")

        # Check para metodos duplicados
        unique_methods = set()
        for method in methods:
            if method in unique_methods:
                raise ValueError(f"Método duplicado '{method}' en la definición de clase")
            unique_methods.add(method)

        self.classes[class_name] = {
            "superclass": superclass_name,
            "methods": methods
        }

    def describe_class(self, class_name):
        """
        Imprime la tabla de métodos para una clase.
        """
        if class_name not in self.classes:
            raise ValueError(f"Class '{class_name}' no existe")

        vtable = {}
        self._build_vtable(class_name, vtable)

        for method, implementation in vtable.items():
            print(f"{method} -> {implementation}")

    def _build_vtable(self, class_name, vtable):
        superclass = self.classes[class_name]["superclass"]
        if superclass:
            self._build_vtable(superclass, vtable)

        for method in self.classes[class_name]["methods"]:
            vtable[method] = f"{class_name}::{method}"

    def start(self):
        """
        Inicia el manejador y procede a realizar una acción para CLASS DESCRIBRIR ó SALIR

        """
        while True:
            command = input("Ingrese un comando CLASS, DESCRIBIR ó SALIR: ").strip()
            if command.startswith("CLASS"):
                try:
                    self.define_class(command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command.startswith("DESCRIBIR"):
                parts = command.split()
                if len(parts) != 2:
                    print("Error: comando invalido DESCRIBIR")
                    continue

                try:
                    self.describe_class(parts[1])
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "SALIR":
                print("Saliendo...")
                break
            else:
                print("Error: Comando desconocido")

# Example usage:
if __name__ == "__main__":
    manager = ClassManager()
    manager.start()
