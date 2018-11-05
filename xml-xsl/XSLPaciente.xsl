<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Datos Paciente</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>idPaciente</th>
      <th>NUSS</th>
      <th>Nombre</th>
      <th>Apellidos</th>
      <th>Sexo</th>
      <th>Fecha de Nacimiento</th>
      <th>Domicilio</th>
      <th>Localidad</th>
      <th>Correo electronico</th>
      <th>Telefono</th>
      <th>Embarazada</th>
    </tr>
    <xsl:for-each select="bbTrack/Paciente">
    <tr>
      <td><xsl:value-of select="@idPaciente"/></td>
      <td><xsl:value-of select="NUSS"/></td>
      <td><xsl:value-of select="Nombre"/></td>
      <td><xsl:value-of select="Apellidos"/></td>
      <td><xsl:value-of select="Sexo"/></td>
      <td><xsl:value-of select="Fecha_nacimiento"/></td>
      <td><xsl:value-of select="Domicilio"/></td>
      <td><xsl:value-of select="Localidad"/></td>
      <td><xsl:value-of select="Correo_electronico"/></td>
      <td><xsl:value-of select="Telefono"/></td>
      <td><xsl:value-of select="Embarazada"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>