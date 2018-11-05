<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Vista General</h2>
  <h2>Lista de pacientes</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>idPaciente</th>
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Pacientes/Paciente">
    <tr>
      <td bgcolor="#F2F5A9">
      	<xsl:variable name = "name"> 
    		<xsl:value-of select="@idPaciente"/>.xml
      	</xsl:variable>
      		<a href="{$name}">    		
      			<xsl:value-of select="@idPaciente"/>
          </a> 
  	  </td>
      <td><xsl:value-of select="Nombre"/></td>

      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  <h2>Lista de medicos</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Licencia</th>
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Medicos/Medico">
    <tr>
      <td bgcolor="#F2F5A9">
        <xsl:variable name = "name"> 
        <xsl:value-of select="@Licencia"/>.xml
        </xsl:variable>
          <a href="{$name}">        
            <xsl:value-of select="@Licencia"/>
          </a> 
      </td>
            <td><xsl:value-of select="Nombre"/></td>

      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  <h2>Lista de enfermedades</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Codigo</th>
      <th>Nombre</th>
    </tr>
    <xsl:for-each select="bbTrack/ICD_10_Pregnancy/ICD_10">
    <tr>
      <td><xsl:value-of select="@Codigo"/></td>
      <td><xsl:value-of select="Nombre"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>