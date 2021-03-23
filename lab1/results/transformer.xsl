<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output
        indent="yes"
        method="xml"
        doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
        doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" />
    <xsl:template match="/">
        <html>
            <head>
                <title>portativ.ua</title>
            </head>
            <body>
                <h2>Products</h2>
                <table border="1">
                    <thead>
                        <tr>
                            <td>Image</td>
                            <td>Name</td>
                            <td>Price in UAH</td>
                        </tr>
                    </thead>
                    <tbody>
                        <xsl:for-each select="data/product">
                            <tr>
                                <td><xsl:apply-templates select="image"/></td>
                                <td><xsl:value-of select="description"/></td>
                                <td><xsl:value-of select="price"/></td>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="image">
         <img alt="image of product">
            <xsl:attribute name="src">
                <xsl:value-of select="text()"/>
            </xsl:attribute>
        </img>
    </xsl:template>
</xsl:stylesheet>
