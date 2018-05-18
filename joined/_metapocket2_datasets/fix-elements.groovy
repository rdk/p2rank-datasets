/**
 * fix pdb files that have no element column (like those in metapocket2 datasets)
 */

void overwrite(String fname, Object text) {
    File file = new File(fname)
    if (file.exists()) {
        file.delete()
    }
    file.createNewFile()
    file.write(text.toString())
}

String dir = args[0]
def outdir = "$dir/fixed"
new File(outdir).mkdirs()

new File(dir).eachFileMatch(~/.*\.pdb/) { File file ->

    def fname = file.name
    println "processing $fname ..."
    List<String> lines =  file.readLines()
    List<String> newLines = new ArrayList<>()

    for (String line in lines) {
        if (line.startsWith("ATOM") && (line.length()<78 || !Character.isAlphabetic((int)line.charAt(77) )) ) {       // !Character.isAlphabetic(line.charAt(77)

            String newLine = line.substring(0, 76) + " " + line.charAt(13)

            //println "/ $line"
            //println "\\ $newLine"

            newLines.add(newLine)
        } else {
            newLines.add(line)
        }
    }

    def outfile = "$outdir/$fname"
    overwrite(outfile, newLines.join("\n")+"\n")
}













