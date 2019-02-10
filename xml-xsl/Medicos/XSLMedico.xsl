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
  <h2>Datos Medico</h2>
  <table border="1" class="table display table-hover">
    <tr bgcolor="#9acd32">
      <th>Licencia</th>
      <th>Nombre</th>
      <th>Apellidos</th>
      <th>Sexo</th>
      <th>Especialidad</th>
      <th>Consultas</th>      
    </tr>
    <xsl:for-each select="bbTrack/Medico">
    <tr>
      <td><xsl:value-of select="@Licencia"/></td>
      <td><xsl:value-of select="Nombre"/></td>
      <td><xsl:value-of select="Apellidos"/></td>
      <td><xsl:value-of select="Sexo"/></td>
      <td><xsl:value-of select="Especialidad"/></td>
      <td><xsl:value-of select="Consultas"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>