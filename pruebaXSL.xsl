<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Lista de pacientes</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>idPaciente</th>
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Paciente">
    <tr>
      <td><xsl:value-of select="@idPaciente"/></td>
      <td><xsl:value-of select="Nombre"/></td>
      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  <h2>Lista de medicos</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Nombre</th>
      <th>Apellidos</th>
    </tr>
    <xsl:for-each select="bbTrack/Medico">
    <tr>
      <td><xsl:value-of select="Nombre"/></td>
      <td><xsl:value-of select="Apellidos"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>