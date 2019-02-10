<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <head>
    <link rel="stylesheet" href="style.css" type="text/css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"/>

  </head>
  <body>
  <h1>bbTrack</h1>
  <h2>Lista de pacientes</h2>
  <table border="1" class="table display table-hover">
    <tr bgcolor="#9acd32">
      <th>idPaciente</th>
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Pacientes/Paciente">
    <tr>
      <td>
      	<xsl:variable name = "name"> 
    		<xsl:value-of select="@idPaciente"/>.xml
      	</xsl:variable>
      		<a href="Pacientes/{$name}">    		
      			<xsl:value-of select="@idPaciente"/>
          </a> 
  	  </td>
      <td><xsl:value-of select="Nombre"/></td>

      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  <h2>Lista de medicos</h2>
  <table border="1" class="table display table-hover">
    <tr bgcolor="#9acd32">
      <th>Licencia</th>
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Medicos/Medico">
    <tr>
      <td>
        <xsl:variable name = "name"> 
        <xsl:value-of select="@Licencia"/>.xml
        </xsl:variable>
          <a href="Medicos/{$name}">        
            <xsl:value-of select="@Licencia"/>
          </a> 
      </td>
            <td><xsl:value-of select="Nombre"/></td>

      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  <h2>Lista de enfermedades</h2>
  <table border="1" class="table display table-hover">
    <tr bgcolor="#9acd32">
      <th>Codigo</th>
      <th>Nombre</th>
    </tr>
    <xsl:for-each select="bbTrack/ICD_10_Pregnancy/ICD_10">
    <tr>
      <td>
          <a href="http://apps.who.int/classifications/icd10/browse/2010/en#/XV">        
            <xsl:value-of select="@Codigo"/>
          </a> 
      </td>
      <td><xsl:value-of select="Nombre"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>