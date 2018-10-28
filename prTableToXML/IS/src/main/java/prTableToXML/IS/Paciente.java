package prTableToXML.IS;

public class Paciente {

	public String idPaciente;
	public String NUSS;
	public String Nombre;
	public String Apellidos;
	public String Sexo;
	public String Fecha_nacimiento;
	public String Domicilio;
	public String Localidad;
	public String Correo_electronico;
	public String Telefono;
	public boolean Embarazada;
	
	public Paciente(String idPaciente, String NUSS, String Nombre,
			String Apellidos, String Sexo, String Fecha_nacimiento, String Domicilio, 
			String Localidad, String Correo_electrónico, String Telefono, Boolean Embarazada) {
		this.idPaciente =  idPaciente;
		this.NUSS = NUSS;
		this.Nombre = Nombre;
		this.Apellidos = Apellidos;
		this.Sexo = Sexo;
		this.Fecha_nacimiento = Fecha_nacimiento;
		this.Domicilio = Domicilio;
		this.Localidad = Localidad;
		this.Correo_electronico = Correo_electrónico;
		this.Telefono = Telefono;
		this.Embarazada = Embarazada;
				
	}




	

	
	
}
